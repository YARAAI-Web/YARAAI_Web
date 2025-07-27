rule auto_rule_20250726202058_0813 {
  strings:
    $o0 = "dword_418348" wide ascii nocase
    $o1 = "off_401800" wide ascii nocase
  condition:
    all of them
}