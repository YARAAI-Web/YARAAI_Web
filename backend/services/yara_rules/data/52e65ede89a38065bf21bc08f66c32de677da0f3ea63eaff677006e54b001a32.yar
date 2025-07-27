rule auto_rule_20250727030233_7786 {
  strings:
    $o0 = "dword_782DC" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}