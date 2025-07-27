rule auto_rule_20250726191616_3765 {
  strings:
    $o0 = "GetKeyNameTextW" wide ascii nocase
    $o1 = "lpszDevice" wide ascii nocase
  condition:
    all of them
}