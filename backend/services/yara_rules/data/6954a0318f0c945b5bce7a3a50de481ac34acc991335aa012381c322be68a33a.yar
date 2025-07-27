rule auto_rule_20250726090526_0992 {
  strings:
    $o0 = "dword_40A18C" wide ascii nocase
    $o1 = "dword_4012B4" wide ascii nocase
  condition:
    all of them
}