rule auto_rule_20250726150859_2201 {
  strings:
    $o0 = "__sbh_resize_block" wide ascii nocase
    $o1 = "xFF000000" wide ascii nocase
    $o2 = "x413555" wide ascii nocase
  condition:
    3 of ($o*)
}