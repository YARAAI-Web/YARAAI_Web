rule auto_rule_20250726094854_1479 {
  strings:
    $o0 = "__addlocaleref" wide ascii nocase
    $o1 = "dword_409888" wide ascii nocase
    $o2 = "x101Du" wide ascii nocase
  condition:
    3 of ($o*)
}