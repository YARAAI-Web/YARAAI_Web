rule auto_rule_20250726065743_4088 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "off_44D55C" wide ascii nocase
  condition:
    all of them
}