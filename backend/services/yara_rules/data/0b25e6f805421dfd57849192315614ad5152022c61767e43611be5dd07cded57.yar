rule auto_rule_20250726103830_3678 {
  strings:
    $o0 = "off_464BB8" wide ascii nocase
    $o1 = "dword_4651B8" wide ascii nocase
    $o2 = "Handler" wide ascii nocase
    $o3 = "Program" wide ascii nocase
  condition:
    4 of ($o*)
}