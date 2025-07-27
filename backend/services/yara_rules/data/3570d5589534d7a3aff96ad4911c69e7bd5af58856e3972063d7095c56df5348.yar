rule auto_rule_20250727040440_7932 {
  strings:
    $o0 = "dword_4795F8" wide ascii nocase
    $o1 = "dword_4794D4" wide ascii nocase
    $o2 = "dword_47961C" wide ascii nocase
  condition:
    3 of ($o*)
}