rule auto_rule_20250726105455_8444 {
  strings:
    $o0 = "p_exceptfds" wide ascii nocase
    $o1 = "_Facet_base" wide ascii nocase
    $o2 = "unknown_libname_131" wide ascii nocase
  condition:
    3 of ($o*)
}