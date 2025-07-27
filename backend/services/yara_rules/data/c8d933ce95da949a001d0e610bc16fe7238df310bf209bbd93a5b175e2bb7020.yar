rule auto_rule_20250727043405_7605 {
  strings:
    $o0 = "dword_435438" wide ascii nocase
    $o1 = "dword_435430" wide ascii nocase
    $o2 = "xA1840268" wide ascii nocase
  condition:
    3 of ($o*)
}