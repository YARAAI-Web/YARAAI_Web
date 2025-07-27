rule auto_rule_20250726162052_3111 {
  strings:
    $o0 = "GetUserDefaultLangID" wide ascii nocase
    $o1 = "dword_42C00C" wide ascii nocase
  condition:
    all of them
}