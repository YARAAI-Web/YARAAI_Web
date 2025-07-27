rule auto_rule_20250726143742_9385 {
  strings:
    $o0 = "qword_14003C5A8" wide ascii nocase
    $o1 = "_acrt_stdio_free_buffer_nolock" wide ascii nocase
  condition:
    all of them
}