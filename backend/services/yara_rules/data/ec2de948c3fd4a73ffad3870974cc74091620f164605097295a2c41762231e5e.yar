rule auto_rule_20250726150459_9372 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "off_45C920" wide ascii nocase
    $o2 = "InitializeCriticalSec" wide ascii nocase
    $o3 = "dword_45CF0C" wide ascii nocase
    $o4 = "dword_45CD98" wide ascii nocase
  condition:
    4 of ($o*)
}