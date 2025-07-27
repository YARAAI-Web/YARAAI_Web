rule auto_rule_20250726071619_6653 {
  strings:
    $o0 = "x100010001LL" wide ascii nocase
    $o1 = "x1400013BDLL" wide ascii nocase
    $o2 = "WriteProcessMemory" wide ascii nocase
  condition:
    3 of ($o*)
}