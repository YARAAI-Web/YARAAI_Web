rule auto_rule_20250727012838_7799 {
  strings:
    $o0 = "xFFFFDF8C" wide ascii nocase
    $o1 = "dword_7FC00" wide ascii nocase
  condition:
    all of them
}