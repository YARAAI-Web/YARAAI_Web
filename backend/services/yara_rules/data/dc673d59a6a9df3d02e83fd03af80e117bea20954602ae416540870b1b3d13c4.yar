rule auto_rule_20250726215846_2253 {
  strings:
    $o0 = "j_unknown_libname_45" wide ascii nocase
    $o1 = "ItemDecryptCancel" wide ascii nocase
    $o2 = "j___lseeki64_nolock" wide ascii nocase
  condition:
    3 of ($o*)
}