rule auto_rule_20250726173709_3513 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "dword_40E01C" wide ascii nocase
    $o2 = "_except_handler3" wide ascii nocase
    $o3 = "dword_41158C" wide ascii nocase
    $o4 = "x41C4u" wide ascii nocase
  condition:
    4 of ($o*)
}