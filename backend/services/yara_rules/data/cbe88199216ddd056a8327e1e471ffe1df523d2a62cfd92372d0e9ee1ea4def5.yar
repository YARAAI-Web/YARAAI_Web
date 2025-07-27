rule auto_rule_20250726122104_8835 {
  strings:
    $o0 = "lpszSrc" wide ascii nocase
    $o1 = "lpszFormatName" wide ascii nocase
    $o2 = "cchClassNameMax" wide ascii nocase
    $o3 = "VkKeyScanExW" wide ascii nocase
  condition:
    4 of ($o*)
}