rule auto_rule_20250727021728_3248 {
  strings:
    $o0 = "lprcItem" wide ascii nocase
    $o1 = "hConv" wide ascii nocase
    $o2 = "paccel" wide ascii nocase
    $o3 = "ptScreen" wide ascii nocase
    $o4 = "lpIconName" wide ascii nocase
  condition:
    4 of ($o*)
}