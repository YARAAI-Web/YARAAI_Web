rule auto_rule_20250726191132_4333 {
  strings:
    $o0 = "dword_45CB08" wide ascii nocase
    $o1 = "x12010u" wide ascii nocase
    $o2 = "dword_45C1C4" wide ascii nocase
    $o3 = "dword_45CD88" wide ascii nocase
    $o4 = "CopyUnwindUp_0" wide ascii nocase
  condition:
    4 of ($o*)
}