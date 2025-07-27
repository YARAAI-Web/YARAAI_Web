rule auto_rule_20250727024912_6914 {
  strings:
    $o0 = "word_4C12C8" wide ascii nocase
    $o1 = "x5Bu" wide ascii nocase
    $o2 = "off_4BB5D0" wide ascii nocase
    $o3 = "timeGetTime" wide ascii nocase
  condition:
    4 of ($o*)
}