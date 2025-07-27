rule auto_rule_20250726232633_2770 {
  strings:
    $o0 = "hmenu" wide ascii nocase
    $o1 = "fByPosition" wide ascii nocase
    $o2 = "lprcSrc2" wide ascii nocase
    $o3 = "dword_42A88C" wide ascii nocase
  condition:
    4 of ($o*)
}