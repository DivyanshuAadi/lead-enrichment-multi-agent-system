<#
.SYNOPSIS
Universal 1-Click Installer for Lead Enrichment Multi-Agent Plugin.
Installs plugin to Antigravity, Claude Code, GitHub Copilot, or any target project.
#>
param (
    [string]$TargetDir = ""
)

$SourceDir = $PSScriptRoot

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🚀 INSTALLING LEAD ENRICHMENT MULTI-AGENT PLUGIN" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Install to Antigravity Global Skills
$AntigravitySkills = "$env:USERPROFILE\.agents\skills\lead-enrichment-plugin"
if (-not (Test-Path $AntigravitySkills)) {
    New-Item -ItemType Directory -Force -Path $AntigravitySkills | Out-Null
}
Copy-Item -Path "$SourceDir\SKILL.md" -Destination "$AntigravitySkills\SKILL.md" -Force
Write-Host "✅ Antigravity Skill Installed: $AntigravitySkills\SKILL.md" -ForegroundColor Green

# 2. Install to Claude Code Global Plugins
$ClaudePlugins = "$env:USERPROFILE\.claude\plugins\lead-enrichment-plugin"
if (-not (Test-Path $ClaudePlugins)) {
    New-Item -ItemType Directory -Force -Path $ClaudePlugins | Out-Null
}
Copy-Item -Path "$SourceDir\*" -Destination $ClaudePlugins -Recurse -Force
Write-Host "✅ Claude Code Plugin Installed: $ClaudePlugins" -ForegroundColor Green

# 3. Optional: Copy to Specific Project
if ($TargetDir -and (Test-Path $TargetDir)) {
    Copy-Item -Path "$SourceDir\*" -Destination $TargetDir -Recurse -Force
    Write-Host "✅ Copied Plugin to Target Project: $TargetDir" -ForegroundColor Green
}

Write-Host "`n🎉 INSTALLATION COMPLETE! You can now use the plugin in any coding agent." -ForegroundColor Yellow
