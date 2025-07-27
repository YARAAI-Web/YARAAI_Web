rule auto_rule_20250726145847_7408 {
  strings:
    $o0 = "aCouldNotAddRes" wide ascii nocase
    $o1 = "_except_handler3" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "_cftoe2" wide ascii nocase
  condition:
    4 of ($o*)
}