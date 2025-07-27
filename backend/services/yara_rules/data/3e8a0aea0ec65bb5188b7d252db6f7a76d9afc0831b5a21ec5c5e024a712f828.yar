rule auto_rule_20250727034225_1158 {
  strings:
    $o0 = "uItem" wide ascii nocase
    $o1 = "SetScrollRange" wide ascii nocase
    $o2 = "lprcItem" wide ascii nocase
    $o3 = "GetClassNameA" wide ascii nocase
  condition:
    4 of ($o*)
}