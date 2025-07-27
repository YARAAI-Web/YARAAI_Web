rule auto_rule_20250727010923_9026 {
  strings:
    $o0 = "dword_4693E4" wide ascii nocase
    $o1 = "dword_4673E8" wide ascii nocase
  condition:
    all of them
}