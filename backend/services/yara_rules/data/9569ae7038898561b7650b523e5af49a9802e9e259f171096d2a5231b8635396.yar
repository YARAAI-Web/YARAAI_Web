rule auto_rule_20250726091830_9468 {
  strings:
    $o0 = "byte_443BA8" wide ascii nocase
    $o1 = "dword_4602A0" wide ascii nocase
    $o2 = "dword_45FCC4" wide ascii nocase
    $o3 = "dword_45FE00" wide ascii nocase
  condition:
    4 of ($o*)
}