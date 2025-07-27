rule auto_rule_20250727022104_8615 {
  strings:
    $o0 = "x17000u" wide ascii nocase
    $o1 = "lpWindowName" wide ascii nocase
  condition:
    all of them
}