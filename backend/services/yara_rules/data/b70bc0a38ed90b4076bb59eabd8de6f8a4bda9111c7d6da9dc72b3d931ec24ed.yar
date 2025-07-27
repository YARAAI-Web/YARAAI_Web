rule auto_rule_20250726092848_1882 {
  strings:
    $o0 = "lpwcx" wide ascii nocase
    $o1 = "GetKeyNameTextW" wide ascii nocase
    $o2 = "SetMenuItemInfoA" wide ascii nocase
  condition:
    3 of ($o*)
}