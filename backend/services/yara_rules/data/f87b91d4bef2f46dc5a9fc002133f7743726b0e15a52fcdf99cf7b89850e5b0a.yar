rule auto_rule_20250726145311_5161 {
  strings:
    $o0 = "Runtime" wide ascii nocase
    $o1 = "xD7u" wide ascii nocase
    $o2 = "dword_41223C" wide ascii nocase
  condition:
    3 of ($o*)
}