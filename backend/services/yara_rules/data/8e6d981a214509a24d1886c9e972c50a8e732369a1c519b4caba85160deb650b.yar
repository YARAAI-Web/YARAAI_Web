rule auto_rule_20250726221808_1692 {
  strings:
    $o0 = "C22h" wide ascii nocase
    $o1 = "dword_422982" wide ascii nocase
    $o2 = "dword_42296E" wide ascii nocase
    $o3 = "x678EC805" wide ascii nocase
    $o4 = "dword_422896" wide ascii nocase
  condition:
    4 of ($o*)
}