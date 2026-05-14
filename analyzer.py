from scraper import ProjectData
from typing import List, Dict

def analyze_project(data: ProjectData) -> Dict:
    team_score = _analyze_team(data)
    social_score = _analyze_social(data)
    red_flags = _detect_red_flags(data)
    green_flags = _detect_green_flags(data)
    trust_score = _calculate_trust_score(team_score, social_score, red_flags, green_flags)
    summary = _generate_summary(trust_score)

    return {
        "project_name": data.project_name or _extract_name(data.url),
        "url": data.url,
        "trust_score": trust_score,
        "summary": summary,
        "team_score": team_score,
        "social_score": social_score,
        "red_flags": red_flags,
        "green_flags": green_flags,
        "team": [vars(m) for m in data.team],
        "funding": [vars(f) for f in data.funding],
        "social_links": data.social_links,
    }

def _analyze_team(data: ProjectData) -> int:
    if not data.team:
        return 0
    identified = sum(1 for m in data.team if not m.anonymous)
    has_linkedin = any(m.linkedin for m in data.team)
    score = min(100, identified * 20 + (20 if has_linkedin else 0))
    return score

def _analyze_social(data: ProjectData) -> int:
    score = 0
    if data.social_links.get("twitter"):
        score += 30
    if data.social_links.get("github"):
        score += 30
    if data.social_links.get("discord"):
        score += 20
    if data.social_links.get("linkedin"):
        score += 20
    return min(100, score)

def _detect_red_flags(data: ProjectData) -> List[str]:
    flags = []
    if not data.team:
        flags.append("No team information found")
    else:
        anon = sum(1 for m in data.team if m.anonymous)
        if anon > 0:
            flags.append(f"{anon} anonymous team member(s) detected")
        if not any(m.linkedin for m in data.team):
            flags.append("No LinkedIn profiles found for team")
    if not data.social_links.get("twitter"):
        flags.append("No Twitter/X presence found")
    if not data.social_links.get("github"):
        flags.append("No GitHub repository found")
    if not data.description:
        flags.append("No project description available")
    return flags

def _detect_green_flags(data: ProjectData) -> List[str]:
    flags = []
    identified = sum(1 for m in data.team if not m.anonymous)
    if identified >= 2:
        flags.append("Multiple identified team members")
    if any(m.linkedin for m in data.team):
        flags.append("Team has LinkedIn presence")
    if data.funding:
        flags.append("Funding information available")
    if data.social_links.get("github"):
        flags.append("Open source code available")
    if data.social_links.get("twitter"):
        flags.append("Active Twitter/X presence")
    return flags

def _calculate_trust_score(team: int, social: int, red: List, green: List) -> int:
    score = 50
    score += team * 0.25
    score += social * 0.25
    score -= len(red) * 5
    score += len(green) * 5
    return max(0, min(100, round(score)))

def _generate_summary(score: int) -> str:
    if score >= 80:
        return "High trust. Strong transparency and credibility signals."
    elif score >= 60:
        return "Moderate trust. Some positive signals but verify further."
    elif score >= 40:
        return "Low trust. Several red flags detected. Proceed with caution."
    return "Very low trust. Multiple red flags. High risk."

def _extract_name(url: str) -> str:
    from urllib.parse import urlparse
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts[-1] if parts else parsed.netloc
