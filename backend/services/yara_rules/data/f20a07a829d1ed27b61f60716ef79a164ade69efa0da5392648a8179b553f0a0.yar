rule auto_rule_20250726103308_8238 {
  strings:
    $o0 = "fdwUnprepare" wide ascii nocase
    $o1 = "CodePagea" wide ascii nocase
    $o2 = "_ms_p5_mp_test_fdiv" wide ascii nocase
  condition:
    3 of ($o*)
}