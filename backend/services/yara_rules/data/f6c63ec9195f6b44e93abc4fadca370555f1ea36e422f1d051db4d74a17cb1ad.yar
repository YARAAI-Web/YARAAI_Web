rule auto_rule_20250726192455_5319 {
  strings:
    $o0 = "lpsi" wide ascii nocase
    $o1 = "cchMaxCount" wide ascii nocase
    $o2 = "EnumSystemLanguageGroupsW" wide ascii nocase
    $o3 = "FlushConsoleInputBuffer" wide ascii nocase
  condition:
    4 of ($o*)
}