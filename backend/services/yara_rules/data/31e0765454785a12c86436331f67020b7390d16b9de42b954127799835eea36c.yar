rule auto_rule_20250726101458_9081 {
  strings:
    $o0 = "dword_4C14CC" wide ascii nocase
  condition:
    all of them
}