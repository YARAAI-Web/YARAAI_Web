rule auto_rule_20250726121510_9438 {
  strings:
    $o0 = "dword_4373EC" wide ascii nocase
  condition:
    all of them
}