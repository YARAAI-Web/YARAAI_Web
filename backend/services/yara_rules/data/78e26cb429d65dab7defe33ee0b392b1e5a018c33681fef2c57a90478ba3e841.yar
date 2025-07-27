rule auto_rule_20250726215634_3783 {
  strings:
    $o0 = "pszFileName" wide ascii nocase
    $o1 = "VkKeyScanExA" wide ascii nocase
    $o2 = "uCommand" wide ascii nocase
  condition:
    3 of ($o*)
}