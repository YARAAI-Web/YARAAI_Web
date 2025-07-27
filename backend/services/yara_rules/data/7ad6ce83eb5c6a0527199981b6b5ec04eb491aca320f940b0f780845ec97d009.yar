rule auto_rule_20250726092657_7344 {
  strings:
    $o0 = "ChangeDisplaySettingsExA" wide ascii nocase
    $o1 = "insb" wide ascii nocase
    $o2 = "IMPGetIMEW" wide ascii nocase
    $o3 = "lpSecurityAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}