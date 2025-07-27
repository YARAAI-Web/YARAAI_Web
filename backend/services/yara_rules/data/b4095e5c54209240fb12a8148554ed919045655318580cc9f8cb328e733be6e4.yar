rule auto_rule_20250727000134_4826 {
  strings:
    $o0 = "dword_78568" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}