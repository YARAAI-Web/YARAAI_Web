rule auto_rule_20250726161605_8475 {
  strings:
    $o0 = "strpbrk" wide ascii nocase
    $o1 = "dword_4503E0" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "off_44FB88" wide ascii nocase
  condition:
    4 of ($o*)
}