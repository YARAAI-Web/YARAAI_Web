rule auto_rule_20250727004656_9399 {
  strings:
    $o0 = "dword_42A014" wide ascii nocase
    $o1 = "byte_42901C" wide ascii nocase
  condition:
    all of them
}