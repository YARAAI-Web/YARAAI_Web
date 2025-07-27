rule auto_rule_20250727022021_0231 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "byte_44FD5C" wide ascii nocase
    $o2 = "__sbh_resize_block" wide ascii nocase
  condition:
    3 of ($o*)
}