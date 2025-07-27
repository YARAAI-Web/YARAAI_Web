rule auto_rule_20250726233446_2584 {
  strings:
    $o0 = "back" wide ascii nocase
    $o1 = "qword_14003ED98" wide ascii nocase
    $o2 = "win32_utils_from_utf8" wide ascii nocase
  condition:
    3 of ($o*)
}