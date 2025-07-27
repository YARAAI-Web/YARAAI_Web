rule auto_rule_20250726230252_2605 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "old_esp" wide ascii nocase
    $o3 = "byte_443A58" wide ascii nocase
  condition:
    4 of ($o*)
}