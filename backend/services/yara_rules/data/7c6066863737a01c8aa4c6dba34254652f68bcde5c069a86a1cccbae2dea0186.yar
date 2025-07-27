rule auto_rule_20250727031657_2391 {
  strings:
    $o0 = "xC0000093" wide ascii nocase
    $o1 = "_CrtIsValidPointer" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "Second" wide ascii nocase
    $o4 = "dword_465460" wide ascii nocase
  condition:
    4 of ($o*)
}