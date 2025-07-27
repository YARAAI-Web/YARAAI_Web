rule auto_rule_20250726230122_9056 {
  strings:
    $o0 = "main_loop_entrance_0" wide ascii nocase
    $o1 = "off_45C928" wide ascii nocase
  condition:
    all of them
}