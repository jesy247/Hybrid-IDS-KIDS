#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>
#include <linux/kprobes.h>

// بيشتغل أول ما أي برنامج يفتح
static int handler_pre(struct kprobe *p, struct pt_regs *regs) {
    printk(KERN_INFO "KIDS ALERT: [PID: %d] Program '%s' is trying to run!\n", 
           current->pid, current->comm);
    return 0;
}

static struct kprobe kp = {
    .symbol_name = "do_execve", // مراقبة تشغيل البرامج
};

static int __init ids_init(void) {
    kp.pre_handler = handler_pre;
    register_kprobe(&kp);
    printk(KERN_INFO "KIDS: Module Loaded Successfully\n");
    return 0;
}

static void __exit ids_exit(void) {
    unregister_kprobe(&kp);
    printk(KERN_INFO "KIDS: Module Unloaded\n");
}

module_init(ids_init);
module_exit(ids_exit);
MODULE_LICENSE("GPL");