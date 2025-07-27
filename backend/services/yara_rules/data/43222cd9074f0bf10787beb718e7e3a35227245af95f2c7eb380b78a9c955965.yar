rule auto_rule_20250726133142_3371 {
  strings:
    $o0 = "uEnable" wide ascii nocase
    $o1 = "dword_420B4C" wide ascii nocase
    $o2 = "CopyRect" wide ascii nocase
  condition:
    3 of ($o*)
}