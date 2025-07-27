rule auto_rule_20250726175837_8227 {
  strings:
    $o0 = "dword_10082CEC" wide ascii nocase
  condition:
    all of them
}