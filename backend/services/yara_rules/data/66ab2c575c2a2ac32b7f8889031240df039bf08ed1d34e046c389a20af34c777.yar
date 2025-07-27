rule auto_rule_20250727011646_0453 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "_onexit_lk" wide ascii nocase
    $o2 = "CodePagea" wide ascii nocase
    $o3 = "off_462CC4" wide ascii nocase
    $o4 = "x12010u" wide ascii nocase
  condition:
    5 of ($o*)
}