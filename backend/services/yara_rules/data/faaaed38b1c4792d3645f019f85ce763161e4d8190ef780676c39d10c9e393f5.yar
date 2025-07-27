rule auto_rule_20250726131807_1615 {
  strings:
    $o0 = "VkKeyScanW" wide ascii nocase
    $o1 = "dwExStyle" wide ascii nocase
    $o2 = "GetDlgItemTextW" wide ascii nocase
  condition:
    3 of ($o*)
}