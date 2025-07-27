rule auto_rule_20250726095906_1680 {
  strings:
    $o0 = "opencl" wide ascii nocase
    $o1 = "qword_1407866B8" wide ascii nocase
    $o2 = "qword_14078C968" wide ascii nocase
  condition:
    3 of ($o*)
}